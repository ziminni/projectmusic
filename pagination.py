from Duration import sec_to_min

class Pagination:
    def __init__(self, items, items_per_page=10):
        self.items = items
        self.items_per_page = items_per_page
        self.current_page = 0

    def total_pages(self):
        return (len(self.items) + self.items_per_page - 1) // self.items_per_page

    def get_page_items(self, page=None):
        if page is None:
            page = self.current_page  # Default to current page
        return self.items[self.start_index(page):self.end_index(page)]

    def next_page(self):
        if self.current_page < self.total_pages():
            self.current_page += 1
        return self.get_page_items(self.current_page)

    def previous_page(self):
        if self.current_page > 1:
            self.current_page -= 1
        return self.get_page_items(self.current_page)

    def reset(self):
        self.current_page = 1

    def start_index (self):
        start = (self.current_page - 1) * self.items_per_page
        return start
    
    def end_index (self):
        end = self.start_index() + self.items_per_page
        return end
    

