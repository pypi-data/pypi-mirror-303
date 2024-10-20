import pytest
import yaml
from pathlib import Path
import sys
import os
import platform

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from treemapper.treemapper import read_ignore_file, should_ignore, build_tree, write_yaml_node, main, load_pathspec


@pytest.fixture
def temp_directory(tmp_path):
    # Create a temporary directory structure for testing
    (tmp_path / "dir1").mkdir()
    (tmp_path / "dir1" / "file1.txt").write_text("Content of file1")
    (tmp_path / "dir2").mkdir()
    (tmp_path / "dir2" / "file2.py").write_text("print('Hello, World!')")
    (tmp_path / ".gitignore").write_text("*.log\n")
    return tmp_path


def test_read_ignore_file(temp_directory):
    ignore_file = temp_directory / ".treemapperignore"
    ignore_file.write_text("*.txt\ndir1\n*.class\n")
    ignore_patterns = read_ignore_file(ignore_file)
    assert "*.txt" in ignore_patterns
    assert "dir1" in ignore_patterns
    assert "*.class" in ignore_patterns


def test_should_ignore():
    # Combined patterns: *.txt, dir1, file[1-3].py, log/**
    combined_patterns = ["*.txt", "dir1", "file[1-3].py", "log/**"]
    combined_spec = load_pathspec(combined_patterns)
    assert should_ignore("file.txt", combined_spec)
    assert should_ignore("dir1", combined_spec)
    assert should_ignore("file2.py", combined_spec)
    assert should_ignore(os.path.join("log", "subdir", "file.log"), combined_spec)
    assert not should_ignore("file4.py", combined_spec)
    assert not should_ignore("dir2", combined_spec)
    assert not should_ignore("directory", combined_spec)


def test_build_tree(temp_directory):
    combined_patterns = []
    combined_spec = load_pathspec(combined_patterns)
    tree = build_tree(temp_directory, temp_directory, combined_spec)
    assert len(tree) == 3  # dir1, dir2, and .gitignore
    assert any(node["name"] == "dir1" for node in tree)
    assert any(node["name"] == "dir2" for node in tree)
    assert any(node["name"] == ".gitignore" for node in tree)


def test_write_yaml_node(tmp_path):
    node = {
        "name": "test_dir",
        "type": "directory",
        "children": [
            {
                "name": "test_file.txt",
                "type": "file",
                "content": "Test content"
            }
        ]
    }
    output_file = tmp_path / "test_output.yaml"
    with output_file.open('w') as f:
        write_yaml_node(f, node)

    content = output_file.read_text()
    assert "- name: test_dir" in content
    assert "type: directory" in content
    assert "- name: test_file.txt" in content
    assert "type: file" in content
    assert "content: |" in content
    assert "Test content" in content


# Integration test
def test_main_integration(temp_directory, monkeypatch, capsys):
    monkeypatch.setattr('sys.argv', ['treemapper', str(temp_directory)])
    main()
    captured = capsys.readouterr()
    assert "Directory tree saved to" in captured.out

    output_file = Path.cwd() / "directory_tree.yaml"
    assert output_file.exists()
    content = output_file.read_text()
    assert temp_directory.name in content
    assert "dir1" in content
    assert "dir2" in content
    assert "file1.txt" in content
    assert "file2.py" in content


@pytest.fixture
def complex_directory(tmp_path):
    # Create a more complex temporary directory structure for testing
    (tmp_path / "dir1").mkdir()
    (tmp_path / "dir1" / "file1.txt").write_text("Content of file1")
    (tmp_path / "dir1" / "file2.py").write_text("print('Hello from file2')")
    (tmp_path / "dir2").mkdir()
    (tmp_path / "dir2" / "subdir").mkdir()
    (tmp_path / "dir2" / "subdir" / "file3.log").write_text("Log content")
    (tmp_path / "dir2" / "file4.txt").write_text("Content of file4")
    (tmp_path / "dir2" / "file5.class").write_text("Compiled class content")
    (tmp_path / ".gitignore").write_text("*.log\n")
    (tmp_path / ".treemapperignore").write_text("*.txt\ndir1\n*.class\n")
    # Only create symlink on non-Windows platforms
    if platform.system() != "Windows":
        (tmp_path / "symlink").symlink_to(tmp_path / "dir1")
    return tmp_path


def test_read_ignore_file_with_comments(tmp_path):
    ignore_file = tmp_path / ".treemapperignore"
    ignore_file.write_text("*.txt\n# This is a comment\ndir1\n\n# Another comment\n*.log\n*.class")
    ignore_patterns = read_ignore_file(ignore_file)
    assert "*.txt" in ignore_patterns
    assert "dir1" in ignore_patterns
    assert "*.log" in ignore_patterns
    assert "*.class" in ignore_patterns
    assert "# This is a comment" not in ignore_patterns
    assert "# Another comment" not in ignore_patterns
    assert "" not in ignore_patterns


def test_build_tree_with_ignore_patterns(complex_directory):
    ignore_patterns = read_ignore_file(complex_directory / ".treemapperignore")
    combined_spec = load_pathspec(ignore_patterns)
    tree = build_tree(complex_directory, complex_directory, combined_spec)

    # Check that the ignored directory and files are not in the tree
    assert not any(node["name"] == "dir1" for node in tree)
    assert not any(node["name"] == "file1.txt" for node in tree)
    assert not any(node["name"] == "file4.txt" for node in tree)
    assert not any(node["name"] == "file5.class" for node in tree)

    # Check that non-ignored items are in the tree
    assert any(node["name"] == "dir2" for node in tree)
    assert any(node["name"] == ".gitignore" for node in tree)
    assert any(node["name"] == ".treemapperignore" for node in tree)

    # Check that symlinks are handled correctly (ignored in this case)
    if platform.system() != "Windows":
        assert not any(node["name"] == "symlink" for node in tree)


def test_write_yaml_node_with_unicode(tmp_path):
    node = {
        "name": "test_dir",
        "type": "directory",
        "children": [
            {
                "name": "unicode_file.txt",
                "type": "file",
                "content": "Content with unicode: ÜñíçÕdê"
            }
        ]
    }
    output_file = tmp_path / "test_output.yaml"
    with output_file.open('w', encoding='utf-8') as f:
        write_yaml_node(f, node)

    with output_file.open('r', encoding='utf-8') as f:
        content = f.read()
    assert "Content with unicode: ÜñíçÕdê" in content


def test_main_with_custom_ignore_and_output(complex_directory, tmp_path, monkeypatch, capsys):
    custom_ignore = tmp_path / "custom_ignore"
    custom_ignore.write_text("*.py\n*.class\n")
    custom_output = tmp_path / "custom_output.yaml"

    monkeypatch.setattr('sys.argv', [
        'treemapper',
        str(complex_directory),
        '-i', str(custom_ignore),
        '-o', str(custom_output)
    ])
    main()
    captured = capsys.readouterr()
    assert f"Directory tree saved to {custom_output}" in captured.out

    assert custom_output.exists()
    with custom_output.open('r') as f:
        content = yaml.safe_load(f)

    def check_no_py_or_class_files(node):
        if node['type'] == 'file':
            assert not node['name'].endswith('.py')
            assert not node['name'].endswith('.class')
        elif node['type'] == 'directory' and node.get('children'):
            for child in node['children']:
                check_no_py_or_class_files(child)

    check_no_py_or_class_files(content)


def test_ignore_multiple_patterns(complex_directory, tmp_path, monkeypatch, capsys):
    custom_ignore = tmp_path / "custom_ignore"
    custom_ignore.write_text("*.py\n*.class\ndir2/subdir/*.log\n")
    custom_output = tmp_path / "custom_output.yaml"

    monkeypatch.setattr('sys.argv', [
        'treemapper',
        str(complex_directory),
        '-i', str(custom_ignore),
        '-o', str(custom_output)
    ])
    main()
    captured = capsys.readouterr()
    assert f"Directory tree saved to {custom_output}" in captured.out

    assert custom_output.exists()
    with custom_output.open('r') as f:
        content = yaml.safe_load(f)

    def check_specific_ignores(node):
        if node['type'] == 'file':
            assert not node['name'].endswith('.py')
            assert not node['name'].endswith('.class')
            assert not (node['name'] == 'file3.log')  # Specific pattern
        elif node['type'] == 'directory' and node.get('children'):
            for child in node['children']:
                check_specific_ignores(child)

    check_specific_ignores(content)


def test_ignore_nested_patterns(complex_directory, tmp_path, monkeypatch, capsys):
    # Adding a nested pattern
    custom_ignore = tmp_path / "custom_ignore"
    custom_ignore.write_text("logs/**/*.class\n")
    custom_output = tmp_path / "custom_output.yaml"

    # Add nested .class file
    (complex_directory / "logs").mkdir()
    (complex_directory / "logs" / "nested").mkdir()
    (complex_directory / "logs" / "nested" / "file6.class").write_text("Nested class file content")

    monkeypatch.setattr('sys.argv', [
        'treemapper',
        str(complex_directory),
        '-i', str(custom_ignore),
        '-o', str(custom_output)
    ])
    main()
    captured = capsys.readouterr()
    assert f"Directory tree saved to {custom_output}" in captured.out

    assert custom_output.exists()
    with custom_output.open('r') as f:
        content = yaml.safe_load(f)

    def check_no_nested_class_files(node):
        if node['type'] == 'file':
            assert not node['name'].endswith('.class')
        elif node['type'] == 'directory' and node.get('children'):
            for child in node['children']:
                check_no_nested_class_files(child)

    check_no_nested_class_files(content)


def test_error_handling(tmp_path, monkeypatch, capsys):
    non_existent_dir = tmp_path / "non_existent"
    monkeypatch.setattr('sys.argv', ['treemapper', str(non_existent_dir)])

    with pytest.raises(SystemExit):
        main()

    captured = capsys.readouterr()
    assert "Error: The path" in captured.err
    assert "is not a valid directory" in captured.err


if __name__ == "__main__":
    pytest.main()
