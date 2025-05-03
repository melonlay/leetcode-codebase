import collections


class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        self.expression = expression
        self.idx = 0
        result_set = self._parse_expression()
        return sorted(list(result_set))

    # expression = term | term, expression
    def _parse_expression(self) -> set[str]:
        result_union = set()
        while True:
            term_set = self._parse_term()
            result_union.update(term_set)
            if self.idx < len(self.expression) and self.expression[self.idx] == ',':
                self.idx += 1  # consume ','
            else:
                break  # End of expression segment or '}'
        return result_union

    # term = factor | factor term
    def _parse_term(self) -> set[str]:
        # Start with a set containing an empty string for Cartesian product identity
        result_product = {''}
        while self.idx < len(self.expression) and self.expression[self.idx] not in ',}':
            factor_set = self._parse_factor()

            # Perform Cartesian product
            next_product = set()
            for s1 in result_product:
                for s2 in factor_set:
                    next_product.add(s1 + s2)
            result_product = next_product
            # If result_product becomes empty (e.g., multiplying by empty set from {}), stop
            if not result_product:
                break
        return result_product

    # factor = { expression } | letter | letter factor
    def _parse_factor(self) -> set[str]:
        if self.expression[self.idx] == '{':
            self.idx += 1  # consume '{'
            factor_set = self._parse_expression()
            self.idx += 1  # consume '}'
            return factor_set
        else:  # It's a letter
            word = ""
            start_idx = self.idx
            while self.idx < len(self.expression) and 'a' <= self.expression[self.idx] <= 'z':
                self.idx += 1
            word = self.expression[start_idx:self.idx]
            return {word}
