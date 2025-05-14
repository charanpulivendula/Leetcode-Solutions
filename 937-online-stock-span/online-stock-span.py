class StockSpanner:

    def __init__(self):
        self.stocks = []

    def next(self, price: int) -> int:
        agg = 1
        while self.stocks and self.stocks[-1][0]<=price:
            agg += self.stocks.pop()[1]
        self.stocks.append((price,agg))
        
        return agg
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)