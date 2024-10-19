import pytest
from unittest.mock import MagicMock, patch, mock_open

from ara_cli.file_classifier import FileClassifier
from ara_cli.classifier import Classifier


@pytest.fixture
def mock_file_system():
    return MagicMock()

@pytest.fixture
def mock_classifier():
    with patch.object(Classifier, 'ordered_classifiers', return_value=['py', 'txt', 'bin']):
        yield

def test_file_classifier_init(mock_file_system):
    classifier = FileClassifier(mock_file_system)
    assert classifier.file_system == mock_file_system

def test_read_file_content(mock_file_system):
    classifier = FileClassifier(mock_file_system)
    test_file_path = "test_file.txt"
    test_file_content = "This is a test file."

    with patch("builtins.open", mock_open(read_data=test_file_content)) as mock_file:
        content = classifier.read_file_content(test_file_path)
        mock_file.assert_called_once_with(test_file_path, 'r', encoding='utf-8')
        assert content == test_file_content

def test_is_binary_file(mock_file_system):
    classifier = FileClassifier(mock_file_system)
    test_binary_file_path = "test_binary_file.bin"
    test_text_file_path = "test_text_file.txt"
    binary_content = b'\x00\x01\x02\x03\x04\x80\x81\x82\x83'
    text_content = "This is a text file."

    with patch("builtins.open", mock_open(read_data=binary_content)) as mock_file:
        result = classifier.is_binary_file(test_binary_file_path)
        mock_file.assert_called_once_with(test_binary_file_path, 'rb')
        assert result is True

    with patch("builtins.open", mock_open(read_data=text_content.encode('utf-8'))) as mock_file:
        result = classifier.is_binary_file(test_text_file_path)
        mock_file.assert_called_once_with(test_text_file_path, 'rb')
        assert result is False

    with patch("builtins.open", side_effect=Exception("Unexpected error")):
        result = classifier.is_binary_file(test_binary_file_path)
        assert result is False

def test_read_file_with_fallback(mock_file_system):
    classifier = FileClassifier(mock_file_system)
    test_file_path = "test_file.txt"
    utf8_content = 'This is a test file.'
    latin1_content = 'This is a test file with latin1 encoding.'

    with patch("builtins.open", mock_open(read_data=utf8_content)) as mock_file:
        content = classifier.read_file_with_fallback(test_file_path)
        mock_file.assert_called_once_with(test_file_path, 'r', encoding='utf-8')
        assert content == utf8_content

    with patch("builtins.open", mock_open(read_data=utf8_content)) as mock_file:
        mock_file.side_effect = [UnicodeDecodeError("mock", b"", 0, 1, "reason"), mock_open(read_data=latin1_content).return_value]
        content = classifier.read_file_with_fallback(test_file_path)
        assert content == latin1_content

    with patch("builtins.open", mock_open(read_data=utf8_content)) as mock_file:
        mock_file.side_effect = [UnicodeDecodeError("mock", b"", 0, 1, "reason"), UnicodeDecodeError("mock", b"", 0, 1, "reason")]
        content = classifier.read_file_with_fallback(test_file_path)
        assert content is None

def test_file_contains_tags(mock_file_system):
    classifier = FileClassifier(mock_file_system)
    test_file_path = "test_file.txt"
    file_content = "tag1 tag2 tag3"

    with patch.object(classifier, 'read_file_with_fallback', return_value=file_content):
        result = classifier.file_contains_tags(test_file_path, ['tag1', 'tag2'])
        assert result is True

        result = classifier.file_contains_tags(test_file_path, ['tag1', 'tag4'])
        assert result is False

        with patch.object(classifier, 'read_file_with_fallback', return_value=None):
            result = classifier.file_contains_tags(test_file_path, ['tag1', 'tag2'])
            assert result is False

def test_classify_file(mock_file_system, mock_classifier):
    classifier = FileClassifier(mock_file_system)
    test_file_path = "test_file.py"

    with patch.object(classifier, 'is_binary_file', return_value=False), \
         patch.object(classifier, 'file_contains_tags', return_value=True):
        result = classifier.classify_file(test_file_path, tags=['tag1'])
        assert result == 'py'

    with patch.object(classifier, 'is_binary_file', return_value=True):
        result = classifier.classify_file(test_file_path, tags=['tag1'])
        assert result is None

    with patch.object(classifier, 'file_contains_tags', return_value=False):
        result = classifier.classify_file(test_file_path, tags=['tag1'])
        assert result is None

def test_classify_files_no_tags(mock_file_system, mock_classifier):
    mock_file_system.walk.return_value = [('.', [], ['file1.py', 'file2.txt', 'file3.bin'])]
    mock_file_system.path.join.side_effect = lambda root, file: f"{root}/{file}"

    classifier = FileClassifier(mock_file_system)
    
    with patch.object(classifier, 'classify_file', side_effect=lambda file, _: file.split('.')[-1]):
        result = classifier.classify_files()

    expected = {
        'py': ['./file1.py'],
        'txt': ['./file2.txt'],
        'bin': ['./file3.bin']
    }
    assert result == expected

def test_classify_files_with_tags(mock_file_system, mock_classifier):
    mock_file_system.walk.return_value = [('.', [], ['file1.py', 'file2.txt', 'file3.py'])]
    mock_file_system.path.join.side_effect = lambda root, file: f"{root}/{file}"

    classifier = FileClassifier(mock_file_system)

    with patch.object(classifier, 'classify_file', side_effect=lambda file, tags: 'py' if 'file1' in file else 'txt' if 'file2' in file else None):
        result = classifier.classify_files(tags=['tag1', 'tag2'])

    expected = {
        'py': ['./file1.py'],
        'txt': ['./file2.txt'],
        'bin': []
    }
    assert result == expected

def test_classify_files_with_binary_files(mock_file_system, mock_classifier):
    mock_file_system.walk.return_value = [('.', [], ['file1.py', 'file2.txt', 'file3.bin'])]
    mock_file_system.path.join.side_effect = lambda root, file: f"{root}/{file}"

    classifier = FileClassifier(mock_file_system)

    with patch.object(classifier, 'classify_file', side_effect=lambda file, tags: 'py' if 'file1' in file else 'txt' if 'file2' in file else None):
        result = classifier.classify_files(tags=['tag1', 'tag2'])

    expected = {
        'py': ['./file1.py'],
        'txt': ['./file2.txt'],
        'bin': []
    }
    assert result == expected

def test_classify_files_with_encoding_issues(mock_file_system, mock_classifier):
    mock_file_system.walk.return_value = [('.', [], ['file1.py', 'file2.txt'])]
    mock_file_system.path.join.side_effect = lambda root, file: f"{root}/{file}"

    classifier = FileClassifier(mock_file_system)

    with patch.object(classifier, 'classify_file', side_effect=lambda file, tags: 'py' if 'file1' in file else 'txt' if 'file2' in file else None):
        result = classifier.classify_files(tags=['tag1', 'tag2'])

    expected = {
        'py': ['./file1.py'],
        'txt': ['./file2.txt'],
        'bin': []
    }
    assert result == expected

def test_classify_files_missing_tags(mock_file_system, mock_classifier):
    mock_file_system.walk.return_value = [('.', [], ['file1.py', 'file2.txt'])]
    mock_file_system.path.join.side_effect = lambda root, file: f"{root}/{file}"

    classifier = FileClassifier(mock_file_system)

    with patch.object(classifier, 'classify_file', return_value=None):
        result = classifier.classify_files(tags=['tag1', 'tag2'])

    expected = {
        'py': [],
        'txt': [],
        'bin': []
    }
    assert result == expected

def test_classify_files_skips_binary_files(mock_file_system, mock_classifier):
    mock_file_system.walk.return_value = [('.', [], ['file1.py', 'file2.txt', 'file3.bin'])]
    mock_file_system.path.join.side_effect = lambda root, file: f"{root}/{file}"

    classifier = FileClassifier(mock_file_system)

    with patch.object(classifier, 'is_binary_file', return_value=True):
        result = classifier.classify_files(tags=['tag1', 'tag2'])

    expected = {
        'py': [],
        'txt': [],
        'bin': []
    }
    assert result == expected

def test_print_classified_files(mock_file_system):
    classifier = FileClassifier(mock_file_system)
    files_by_classifier = {
        'python': ['test1.py', 'test2.py'],
        'text': ['test1.txt', 'test2.txt'],
        'binary': []
    }

    with patch("builtins.print") as mock_print:
        classifier.print_classified_files(files_by_classifier)
        mock_print.assert_any_call("Python files:")
        mock_print.assert_any_call("  - test1.py")
        mock_print.assert_any_call("  - test2.py")

        mock_print.assert_any_call("Text files:")
        mock_print.assert_any_call("  - test1.txt")
        mock_print.assert_any_call("  - test2.txt")


def test_classify_file_no_match(mock_file_system, mock_classifier):
    classifier = FileClassifier(mock_file_system)
    test_file_path = "test_file.unknown"

    with patch.object(classifier, 'is_binary_file', return_value=False), \
         patch.object(classifier, 'file_contains_tags', return_value=True):
        result = classifier.classify_file(test_file_path, tags=['tag1'])
        assert result is None
