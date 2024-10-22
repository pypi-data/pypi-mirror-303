# Python package to count web content at a given URL

## Installation
```bash
$ pip install count-web-content
```

## Usage
Simple usage:
```python
count, in_root_count, add_dict, exclude_dict = count_page.count_pages(
    "https://mame77.com/",
    is_print_working=True,
    additional_url=["https://mame77.com/posts/", "https://mame77.com/about"],
    output_url_file_name="output_url.txt",
)
```

### Arguments
- `root_url` : This package counts the number of files in the content of the URL.
- `additional_url` : If specified, You can specify additional URLs to count the number of files.  
This is optional and must be under the same domain as the `root_url`.
- `exclude_url` : If specified, You can specify URLs to exclude from the count.
- `sleep_sec`: The number of seconds to sleep between requests.  
- `is_print_working`: If `True`, the package will print the URL it is currently working on and the number of remaining URLs.
- `output_url_file_name`: If specified, the package will output the URLs to a file.

### Return values
1. `page~count` : The number of files in the content of the URL.
2. `in_root_count` : The number of files in the content of root URL.
3. `additional_dict` : The number of files in the content of additional URLs.
4. `exclude_dict` : The number of files in the content of exclude URLs.