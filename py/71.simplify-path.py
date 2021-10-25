class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = []
        parsed_path = path.split('/')
        for p in parsed_path:
            if len(p) == 0 or p == '.':
                continue
            if p == '..':
                if len(paths) > 0:
                    paths.pop()
                continue
            paths.append(p)
        return '/' + '/'.join(paths)
