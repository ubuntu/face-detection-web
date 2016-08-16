#!/usr/bin/python3

import urllib.request

asset_pattern_to_download = "//assets.ubuntu.com/v1/"
pattern_to_replace_with = "/css/"

if __name__ == "__main__":
    last_pos = 0
    len_pattern = len(asset_pattern_to_download)
    result_css = ""

    with open("ubuntu-styles.css") as f:
        src = f.readlines()[0]
        while True:
            new_replace_index = src.find(asset_pattern_to_download, last_pos)
            if new_replace_index == -1:
                # write content after last pattern
                result_css += src[last_pos:]
                break
            else:
                # write content before pattern
                result_css += src[last_pos:new_replace_index]

                # find end of string
                end_string_candidate1 = src.find('"', new_replace_index)
                end_string_candidate2 = src.find(')', new_replace_index)
                filename_end_pos = end_string_candidate1
                if end_string_candidate2 != -1 and end_string_candidate2 < end_string_candidate1:
                    filename_end_pos = end_string_candidate2
                filename = src[new_replace_index+len_pattern:filename_end_pos]

                # download file
                url = "http:" + asset_pattern_to_download + filename
                print(url)
                urllib.request.urlretrieve(url, filename)

                # rewrite with new url
                new_path = pattern_to_replace_with + filename
                result_css += new_path

                # store new position
                last_pos = filename_end_pos
                
    open("ubuntu-styles.css", 'w').write(result_css)
     
