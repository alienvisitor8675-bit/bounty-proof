To solve this problem, we need to ensure that the `page_bounds` function correctly calculates the start and end indices for each page, including the last item of every full page.

### Approach
The function `page_bounds` is intended to determine the start and end indices for a given page and item size. The issue was that the end index was being set to `start + size - 1`, which caused the last item of each full page to be dropped. The solution is to set the end index as `start + size` to include the correct number of items for each page.

### Solution Code
```python
def page_bounds(page, size):
    start = (page - 1) * size
    end = start + size
    return (start, end)
```

### Explanation
The function `page_bounds` calculates the start index as `(page - 1) * size`, which correctly starts from 0 for the first page. The end index is set to `start + size`, ensuring that each page includes the correct number of items, including the last item of each full page. This adjustment fixes the issue where the last item of each page was being dropped.