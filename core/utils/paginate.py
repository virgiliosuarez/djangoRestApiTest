from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class Paginate:
    nextPage = 1
    previousPage = 1
    numberPage = 5
    data = []

    def paginate_model(self, currentPage, model):
        paginator = Paginator(model, self.numberPage)
        try:
            self.data = paginator.page(currentPage)
        except PageNotAnInteger:
            self.data = paginator.page(1)
        except EmptyPage:
            self.data = paginator.page(paginator.num_pages)

        if self.data.has_next():
            self.nextPage = self.data.next_page_number()
        if self.data.has_previous():
            self.previousPage = self.data.previous_page_number()

        return paginator
