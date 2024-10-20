from files3 import files
import os

def topy(fpath, *, keyword='data', overwrite=False):
    s = files.f3pack(fpath, error=True)
    dirname, basename = os.path.split(fpath)
    pyname = os.path.join(dirname, basename + '.py')
    if os.path.exists(pyname):
        if not overwrite:
            raise FileExistsError(f"File exists: {pyname}. Please set overwrite=True to overwrite it.")
    with open(pyname, 'w', encoding="ascii") as f:
        f.write(f"import files3\nimport os\n\nif not os.path.exists('{basename}'):\n\tfiles3.files.f3unpack(b'")
        for b in s:
            f.write('\\x%02x' % b)
        f.write("', '', error=True)\n")


if __name__ == '__main__':
    topy("dist")
