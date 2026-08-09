from __future__ import annotations

import os
import re
import tempfile
import zipfile
from pathlib import Path
from typing import Iterable, Union
from xml.etree import ElementTree

from docx import Document
from docx.opc.exceptions import OpcError
from lxml.etree import XMLSyntaxError


class UnsafeDocumentError(ValueError):
    pass


_REQUIRED_PARTS = {"[Content_Types].xml", "word/document.xml"}
_EXTERNAL_FIELD = re.compile(
    r"\b(?:DDEAUTO|DDE|INCLUDETEXT|INCLUDEPICTURE|LINK|DATABASE|RD)\b|"
    r"(?:https?|ftp|file):|\\\\|[A-Za-z]:\\",
    re.IGNORECASE,
)


def preflight_docx(path: Union[str, Path]) -> Path:
    candidate = Path(path)
    if not candidate.is_file() or not zipfile.is_zipfile(candidate):
        raise UnsafeDocumentError("Input is not a valid DOCX package.")
    try:
        with zipfile.ZipFile(candidate) as archive:
            infos = archive.infolist()
            names = {item.filename for item in infos}
            lower_names = {name.lower() for name in names}
            if len(names) != len(infos):
                raise UnsafeDocumentError("DOCX contains duplicate package parts.")
            missing = _REQUIRED_PARTS - names
            if missing:
                raise UnsafeDocumentError("DOCX is missing required package parts.")
            if len(infos) > 10_000 or sum(item.file_size for item in infos) > 200 * 1024 * 1024:
                raise UnsafeDocumentError("DOCX package exceeds safe processing limits.")
            xml_parts = [item for item in infos if item.filename.endswith((".xml", ".rels"))]
            if any(
                name == "word/vbaproject.bin"
                or name.startswith("word/embeddings/")
                or name.startswith("word/activex/")
                or name.startswith("word/ctrlprops/")
                for name in lower_names
            ):
                raise UnsafeDocumentError("DOCX contains embedded active or linked content.")
            for item in xml_parts:
                raw = archive.read(item)
                try:
                    root = ElementTree.fromstring(raw)
                except ElementTree.ParseError as exc:
                    raise UnsafeDocumentError("DOCX contains malformed XML.") from exc
                if item.filename.endswith(".rels"):
                    for relationship in root:
                        mode = relationship.attrib.get("TargetMode", "")
                        relationship_type = relationship.attrib.get("Type", "")
                        type_lower = relationship_type.lower()
                        if "activex" in type_lower or type_lower.endswith(("/control", "/controlprop")):
                            raise UnsafeDocumentError("DOCX contains ActiveX or control content.")
                        if mode.lower() == "external" and not relationship_type.endswith("/hyperlink"):
                            raise UnsafeDocumentError("DOCX contains an external relationship.")
                if item.filename == "word/settings.xml":
                    for element in root.iter():
                        if element.tag.endswith("}updateFields"):
                            value = next((v for k, v in element.attrib.items() if k.endswith("}val")), "true")
                            if value.lower() not in {"0", "false", "off", "no"}:
                                raise UnsafeDocumentError("DOCX requests automatic field updates.")
                instructions = "".join((element.text or "") for element in root.iter()
                                       if element.tag.endswith("}instrText"))
                if _EXTERNAL_FIELD.search(instructions):
                    raise UnsafeDocumentError("DOCX contains an external or linked field instruction.")
    except (OSError, zipfile.BadZipFile, RuntimeError) as exc:
        raise UnsafeDocumentError("Input is not a readable DOCX package.") from exc
    return candidate


def load_docx(path: Union[str, Path]):
    safe_path = preflight_docx(path)
    try:
        return Document(str(safe_path))
    except (KeyError, OpcError, TypeError, ValueError, XMLSyntaxError) as exc:
        raise UnsafeDocumentError("Input is not a structurally valid DOCX package.") from exc


def paths_collide(left: Union[str, Path], right: Union[str, Path]) -> bool:
    left_path = Path(left)
    right_path = Path(right)
    if left_path.resolve() == right_path.resolve():
        return True
    if left_path.exists() and right_path.exists():
        try:
            return os.path.samefile(str(left_path), str(right_path))
        except OSError:
            return False
    return False


def validate_output_paths(protected_inputs: Iterable[Union[str, Path]],
                          outputs: Iterable[Union[str, Path]], overwrite: bool = False):
    input_paths = [Path(path) for path in protected_inputs if path is not None]
    output_paths = [Path(path) for path in outputs if path is not None]
    for output in output_paths:
        if any(paths_collide(source, output) for source in input_paths):
            raise ValueError("An output path collides with a protected input path.")
    for index, output in enumerate(output_paths):
        if any(paths_collide(output, other) for other in output_paths[index + 1:]):
            raise ValueError("Two intended output paths collide.")
    for output in output_paths:
        if output.exists() and not output.is_file():
            raise ValueError("An intended output path exists but is not a regular file.")
        if output.exists() and not overwrite:
            raise FileExistsError("An intended output already exists; pass --overwrite to replace it.")
    return output_paths


def publish_atomic(temporary: Union[str, Path], output: Union[str, Path], overwrite: bool) -> None:
    temporary_path = Path(temporary)
    output_path = Path(output)
    if overwrite:
        os.replace(str(temporary_path), str(output_path))
    else:
        os.link(str(temporary_path), str(output_path))
        temporary_path.unlink()


def atomic_write_text(output: Union[str, Path], text: str, overwrite: bool = False) -> Path:
    output_path = Path(output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    handle = tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", prefix=".hnu-report-",
                                         suffix=".tmp", dir=str(output_path.parent), delete=False)
    temporary = Path(handle.name)
    try:
        with handle:
            handle.write(text)
            handle.flush()
            os.fsync(handle.fileno())
        publish_atomic(temporary, output_path, overwrite)
    finally:
        if temporary.exists():
            temporary.unlink()
    return output_path
