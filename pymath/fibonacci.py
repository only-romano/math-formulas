# Fibonacci numbers
class Fibonacci:
    """
    Fibonacci sequence, usage:
    f = Fibonacci()

    CALLABLE.
    f(n:int)
    returns integer, n-th member of fibonacci sequence. Equal to f.get_fib(n).

    f(x,y:int)
    returns a list of integers, which is range of fibonacci sequence with start
    index of "y" and finish index of "x" including both of them.
    Equal to f.get_seq(x, y).

    f([*args]) or f((*args)) or f(*args)
    returns a list of booleans, checks for every element of *args is a fibonacci
    number. Equal to f.is_fibs([*args]).

    f()
    returns string with curent first and second numbers of sequence.

    CLASS METHODS.
    f.is_fib(n:int, (custom:[int,int]))
    returns boolean, check for n is a fibonacci number of given sequence. If
    custom given, sequence starts from custom[0] and custom[1] numbers.

    f.is_fibs(arr:list, (custom:[int,int]))
    returns a list of booleans, checks for every element of *args is a fibonacci
    number of given sequence. If custom given, sequence starts from custom[0]
    and custom[1] numbers.

    f.get_fib(n, (?custom:[int,int]))
    returns integer, n-th member of fibonacci sequence. If custom given,
    sequence starts from custom[0] and custom[1] numbers.

    f.get_seq(_to, (_from:int, custom:[int,int]))
    returns a list of integers, which is range of fibonacci sequence with start
    index of "y" and finish index of "x" including both of them. If custom given,
    sequence starts from custom[0] and custom[1] numbers.

    f.get_sum(n:int, (custom:[int,int]))
    returns integer, sum of fibonacci sequence numbers until n-index. If custom
    given, sequence starts from custom[0] and custom[1] numbers.

    f.get_mean(n:int, (custom:[int,int]))
    returns integer, mean of fibonacci sequence numbers until n-index. If custom
    given, sequence starts from custom[0] and custom[1] numbers.

    f.get_var(n:int, (custom:[int,int]))
    returns integer, variancy of fibonacci sequence numbers until n-index. If
    custom given, sequence starts from custom[0] and custom[1] numbers.

    f.get_dif(n:int, (custom:[int,int]))
    returns integer, mean difference of fibonacci sequence numbers until
    n-index. If custom given, sequence starts from custom[0] and custom[1]
    numbers.
    """
    def __init__(self):
        # custom sequence start numbers
        self.x1 = 0
        self.x2 = 1
        self.custom_flag = False

    def __call__(self, *args):
        if len(args) == 1:
            if isinstance(args[0], int):
                # if class instance called with one integer argument it's envoke
                # find of n-th member of fibonacci sequence function
                return self.get_fib(args[0])
            elif isinstance(args[0], (list, tuple)):
                # if class instance called with a list or tuple argument it's
                # envoke check - is it a fibonacci number for every integer in
                # the list
                return self.is_fibs(*args[0])
        elif len(args) == 2:
            if isinstance(args[0], int) and isinstance(args[1], int):
                # if given two integers arguments, make a range from fibonacci
                # sequence from second arg to first arg indexes
                return self.get_seq(*args)
        elif not len(args):
            # if there is no arguments - return a string
            return self.__str__()
        # if more then two args, check every integer arg is a fibonacci number
        return self.is_fibs(*args)

    def __str__(self):
        return "Fibonacci sequence [" + str(self.x1) \
               + ", " + str(self.x2) + ", ...]"

    def is_fib(self, n, custom=None):
        """
        Integer is a fibonacci number check

        param n:   int, integer to check;
        param custom: None or list of integers, custom start of sequence;
        return:   boolean, n is a fibonacci number of given sequence;
        """
        if n == 0 or n == 1 or n == -1:
            return True
        if not isinstance(n, int):
            # n is not an integer
            return False
        x1, x2, final = 0, 1, abs(n)

        # if custom start numbers set
        if self.custom_flag:
            x1, x2 = abs(self.x1), abs(self.x2)

        # custom sequence
        if custom:
            if len(custom):
                x1 = custom[0]
                if final == x1:
                    return True
                if len(custom) > 1:
                    x2 = custom[1]
                    if final == x2:
                        return True

        while final > x2:
            x1, x2 = x2, x1 + x2
            if final == x2:
                return True
        return False

    def is_fibs(self, *args, custom=None):
        """
        List of integers is a fibonacci numbers check

        param *args:  list of int, integers to check
        param custom: None or list of integers, custom start of sequence;
        return:       list of booleans, list elemenents is a fibonacci numbers
        """
        return [self.is_fib(i, custom) for i in args]

    def get_fib(self, n, custom=None):
        """
        Get n-th member of fibonacci sequence

        param n:  int; index of fibonacci sequence to get a number
        param custom: None or list of integers, custom start of sequence;
        return:   int; n-th member of fibonacci sequence
        """
        x1, check = 0, self.__exceptions(n, 700000)
        if check:
            x2, final = self.__get_starts(n)

            # if custom start numbers set
            if self.custom_flag:
                x1, x2 = self.x1, self.x2
                if n < 0:
                    x1, x2 = -x1, -x2

            # custom sequence
            if custom:
                if len(custom):
                    x1 = custom[0]
                    if n < 0:
                        x1 = -x1
                    elif n == 0:
                        return None

                    if len(custom) > 1:
                        x2 = custom[1]
                        if n < 0:
                            x2 = -x2
                        elif n == 0:
                            return None

            for i in range(final):
                x1, x2 = x2, x1 + x2
            return x2
        return check

    def get_seq(self, _to, _from=0, custom=None):
        '''
        Returns a given range of fibonacci sequence. Both indexes are included.

        param _to:   int [req] - upper index of requested range
        param _from: int [opt] - lower index of requested range, default=0
        param custom: None or list of integers, custom start of sequence;
        returns:   list of int - requested range of fibonacci sequence
        '''
        rev_ord = _from > _to
        if rev_ord: neg_end, pos_end = _to, _from
        else: neg_end, pos_end = _from, _to
        neg = neg_end < 0
        pos = pos_end > 0
        if pos_end < 0: rev_ord = not rev_ord


        def fib_a(self, end, neg=0):
            x1 = 0
            # custom settings
            if self.custom_flag:
                x1 = self.x1
                if neg:
                    x1 = -x1
            # custom sequence given
            if custom and len(custom):
                x1 = custom[0]
                if neg:
                    x1 = -x1
            seq.append(x1)
            if end > 1:
                x2 = neg or 1
                if self.custom_flag:
                    x2 = self.x2
                    if neg:
                        x2 = -x2
                if custom and len(custom) > 1:
                    x2 = custom[1]
                    if neg:
                        x2 = -x2
                seq.append(x2)
                if end > 2:
                    fib_b(x1, x2, end-2)
            neg and seq.reverse()

        def fib_b(x1, x2, reps):
            for i in range(reps):
                x1, x2 = x2, x2 + x1
                seq.append(x2)

        seq = [];
        if neg: fib_a(self, -neg_end, -1)
        if pos: fib_a(self, pos_end)
        if pos_end < 0: seq.reverse()
        seq = seq[-(pos_end-neg_end+1):]
        if rev_ord: seq.reverse()

        return seq

    def get_sum(self, n, custom=None):
        '''
        Sums a numbers from fibonacci sequence

        param n:    int, req; number of members from fibonacci sequence to sum
        param custom: None or list of integers, custom start of sequence;
        returns:    int; sums of n members from fibonacci sequence
        '''
        x1, check = 0, self.__exceptions(n, 500000)
        if check:
            x2, final = self.__get_starts(n)
            # custom sequence
            if self.custom_flag:
                x1, x2 = self.x1, self.x2
            if custom and len(custom):
                x1 = custom[0]
                if len(custom) > 1:
                    x2 = custom[1]
            sum = x1 + x2
            for i in range(final):
                x1, x2 = x2, x1 + x2
                sum += x2
            return sum
        return check

    def get_mean(self, n, custom=None):
        """
        Mean value of fibonacci sequence

        param n: int - final index of sequence
        param custom: None or list of integers, custom start of sequence;
        returns float, mean value of given sequence
        returns integer if n > 1490
        """
        if n > 1490:
            return self.get_sum(n, custom) // n
        return self.get_sum(n, custom) / n

    def get_var(self, n, custom=None):
        """
        Variance value of fibonacci sequence

        param n: int - final index of sequence
        param custom: None or list of integers, custom start of sequence;
        returns float, variance value of given sequence
        returns integer if n > 740
        """
        seq = self.get_seq(n, custom=custom)
        variance = seq[-1]
        sum = 0
        for i in range(n):
            sum += (seq[i] - variance) ** 2
        if n > 740:
            return sum // n
        return sum / n

    def get_dif(self, n, custom=None):
        """
        Mean difference value of fibonacci sequence

        param n: int - final index of sequence
        param custom: None or list of integers, custom start of sequence;
        returns float, mean difference value of given sequence
        returns integer if n > 1477
        """
        seq = self.get_seq(n, custom=custom)
        variance = seq[-1]
        sum = 0
        for i in range(n):
            sum += abs(seq[i] - variance)
        if n > 1477:
            return sum // n
        return sum / n

    def get_ratio(self, n, past=True):
        """
        Ratio of n and sibling fibonacci numbers.

        param n: int - index of fibonacci numbers.
        param past: boolean - flag to pre-sibling, default: True;
        returns float, ratio value of given number and sibling
        """
        if past:
            return self.get_fib(n)/self.get_fib(n-1)
        return self.get_fib(n+1)/self.get_fib(n)

    def get_numbers(self):
        """Get current custom start values, returns tuple (int, int)"""
        return self.x1, self.x2

    def set_numbers(self, numbers):
        """
        Sets current custom start values. Sets custom flag True. This option
        change every function results. To reset in default fibonacci sequence
        run .reset() class method.

        param numbers: list of [int, int], setters for first and second numbers
        of custom sequencce
        """
        self.x1, self.x2 = numbers
        self.custom_flag = True

    def is_custom(self):
        """
        Get custom sequence state. If false, it's default fibonacci sequence
        returns boolean

        """
        return self.custom_flag

    def reset(self):
        """Resets default fibonacci sequence"""
        self.x1, self.x2, self.custom_flag = 0, 1, False

    # property to easy access; f = Fibonacci()
    #
    # getter: f.numbers
    # equal to f.get_numbers()
    #
    # setter: f.numbers = x1, x2
    # equal to f.set_numbers([x1, x2])
    numbers = property(get_numbers, set_numbers)

    @staticmethod
    def __get_starts(n):
        if n > 0:
            return 1, n-2
        return -1, -n-2

    @staticmethod
    def __exceptions(n, m_val):
        if n == 0 or n > m_val or n < -m_val:
            return None
        if n == 1 or n == -1:
            return 0
        return True

# short link
Fibs = Fibonacci

# import
__all__ = ["Fibonacci"]

if __name__ == '__main__':
    f = Fibonacci()
    f.numbers = 8, 40
    print(f.get_ratio(10))
