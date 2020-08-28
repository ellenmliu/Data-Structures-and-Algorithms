import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if not os.path.isdir(path):
        return "Not a valid path"

    if not suffix or len(suffix) <= 0:
        return "Not a valid suffix"

    cur_files = os.listdir(path)
    files = []
    for file in cur_files:
        full_path = os.path.join(path, file)
        if os.path.isdir(full_path):
            files.extend(find_files(suffix, full_path))
        if os.path.isfile(full_path):
            if full_path.endswith(suffix):
                files.append(full_path)

    return files

test_cases = [
{
    "suffix": ".c",
    "path": "testdir",
    "expected": ['testdir/subdir3/subsubdir1/b.c', 'testdir/t1.c', 'testdir/subdir5/a.c', 'testdir/subdir1/a.c']
},
{
    "suffix": ".h",
    "path": "testdir",
    "expected": ['testdir/subdir3/subsubdir1/b.h', 'testdir/subdir5/a.h', 'testdir/t1.h', 'testdir/subdir1/a.h']
},
{
    "suffix": ".py",
    "path": "testdir",
    "expected": []
},
{
    "suffix": "",
    "path": "testdir",
    "expected": "Not a valid suffix"
},
{
    "suffix": ".py",
    "path": "testing",
    "expected": "Not a valid path"
}]

for case in test_cases:
    print("Finding files ending with {} in path {}: ".format(case["suffix"], case["path"]), "pass" if find_files(case["suffix"], case["path"]) == case["expected"] else "fail")
