try:
    from IPython.core.display import clear_output
    have_ipython = True
except ImportError:
    have_ipython = False
class ProgressBar:    
    def __init__(self, iterations, parent_bar = None):
        self.iterations = iterations
        self.parent_bar = parent_bar
        self.prog_bar = '[]'
        self.fill_char = '*'
        self.width = 40
        self.__update_amount(0)
        if have_ipython:
            self.animate = self.animate_ipython
        else:
            self.animate = self.animate_noipython

    def animate_ipython(self, iter, iter_2 = 0):
        import sys
        try:
            clear_output()
        except Exception:
            # terminal IPython has no clear_output
            pass
        
        if self.parent_bar:
            self.parent_bar.animate(iter_2)
            
        self.update_iteration(iter + 1)
        print('\r', self,)
        sys.stdout.flush()
        
            
    def update_iteration(self, elapsed_iter):
        self.__update_amount((elapsed_iter / float(self.iterations)) * 100.0)
        self.prog_bar += '  %d of %s complete' % (elapsed_iter, self.iterations)

    def __update_amount(self, new_amount):
        percent_done = int(round((new_amount / 100.0) * 100.0))
        all_full = self.width - 2
        num_hashes = int(round((percent_done / 100.0) * all_full))
        self.prog_bar = '[' + self.fill_char * num_hashes + ' ' * (all_full - num_hashes) + ']'
        pct_place = int((len(self.prog_bar) / 2) - len(str(percent_done)))
        pct_string = '%d%%' % percent_done
        self.prog_bar = self.prog_bar[0:pct_place] + (pct_string + self.prog_bar[pct_place + len(pct_string):])

    def __str__(self):
        return str(self.prog_bar)
