class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []                      # índices de itens esperando desconto
        res = [0] * len(prices)
        for i, price in enumerate(prices):
            # enquanto o item do topo puder receber desconto do preço atual
            while stack and prices[stack[-1]] >= price:
                j = stack.pop()             # item j encontrou seu desconto
                res[j] = prices[j] - price  # preço dele menos o desconto
            stack.append(i)             # item atual passa a esperar
        # quem sobrou nunca recebeu desconto: fica com o preço original
        while stack:
            j = stack.pop()
            res[j] = prices[j]
        return res