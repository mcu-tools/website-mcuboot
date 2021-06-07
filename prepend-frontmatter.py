import os


def get_md_files(root):
    file_list = []
    for path, subdirs, files in os.walk(root):
        for name in files:
            if name.endswith((".markdown", ".md")):
                file_list.append(os.path.join(path, name))
    return file_list


if __name__ == "__main__":
    markdown_files = get_md_files("./_documentation")
    for markdown_file in markdown_files:
        print("Processing {}".format(markdown_file))
        with open(markdown_file, 'r') as original:
            data = original.read()
        with open(markdown_file, 'w') as modified:
            slug = os.path.basename(markdown_file).split(".")[0]
            modified.write(
                "---\npermalink: /documentation/{}/\n---\n".format(slug) + data)
