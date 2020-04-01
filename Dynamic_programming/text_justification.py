def test_justification(text, column_width):
    """
    Returns the cost and print text after justification
    O(N^2) run-time
    :param text: List[str]
        text to be justified
    :param column_width: int
        required to be larger than max(len(text)) to work
    :return: int
        minimum cost to arrange all words
    """
    import sys
    sum_lens = [0]

    # O(N) cost
    for word in text:
        sum_lens.append(sum_lens[-1] + len(word))

    # O(1) cost
    def cost(i, j):
        """
        calculate cost from putting word i to word j on the same line
        i >= 1
        """
        sum_len = sum_lens[j] - sum_lens[i-1] + (j-i) # j-i blanks for j - i + 1 words
        if sum_len > column_width:
            return sys.maxsize
        else:
            return (column_width - sum_len) ** 3

    L = len(text)
    opt = {L+1: 0}
    linebreaks = [i for i in range(L+1)]

    def top_down(i):
        """
            From which word j >= i should I break the line
        """
        if i not in opt:
            min_cost = sys.maxsize
            for j in range(i, L+1):
                new_cost = cost(i, j) + top_down(j+1)
                if new_cost < min_cost:
                    min_cost = new_cost
                    linebreaks[i] = j
            opt[i] = min_cost
        return opt[i]

    res = top_down(1)

    def print_results(words, breakpoints):
        ix = 1
        while ix < len(words)+1:
            cur = breakpoints[ix]
            print(words[ix-1: cur])
            ix = cur + 1

    # Print text justification
    print_results(text, linebreaks)

    return res


if __name__=='__main__':
    text = 'today is fantastic day and weather is good to go out'.split()
    width = 10
    test_justification(text, width)
    """
    prints:
        ['today', 'is']
        ['fantastic']
        ['day', 'and']
        ['weather']
        ['is', 'good']
        ['to', 'go', 'out']
    """
