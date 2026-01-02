def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    prefix = ""
    for chars in zip(*strs):
        if len(set(chars)) == 1:  # all characters match
            prefix += chars[0]
        else:
            break
    return prefix