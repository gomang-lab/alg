"""
우선순위:
  + , -  → 1
  * , /  → 2
  ^      → 3

결합성:
  + - * /  → 왼쪽 결합 (Left-associative)
  ^        → 오른쪽 결합 (Right-associative) 
  
for token in tokens:
    if 피연산자:
        output에 추가
    elif '(':
        stack에 push
    elif ')':
        '(' 나올 때까지 pop → output
        '(' 제거
    else:  # 연산자
        while (stack이 비어있지 않고
               top이 '('가 아니며
               (top의 우선순위 > 현재 연산자 우선순위
                or
                (우선순위가 같고 현재 연산자가 왼쪽 결합))):
            stack pop → output

        현재 연산자를 stack에 push

남은 stack 전부 pop → output

for token in postfix:
    if 피연산자:
        stack에 push
    else:  # 연산자
        b = stack.pop()
        a = stack.pop()
        결과 = a 연산자 b
        stack에 push

최종 stack[0]이 결과
"""
class Infix2Postfix:
    def __init__(self):
        self.stack = []
        self.output = []

    def precedence(self, op):
        if op in ('+', '-'):
            return 1
        elif op in ('*', '/'):
            return 2
        elif op == '^':
            return 3
        return 0

    def is_right_associative(self, op):
        return op == '^'        

    def is_operand(self, token):
       
        try:
            float(token)
            return True
        except ValueError:
            return False

    def tokenize(self, expression):
        
        tokens = []
        i = 0
        while i < len(expression):
            if expression[i].isspace():
                i += 1
                continue
            if expression[i] in '+-*/^()':
                tokens.append(expression[i])
                i += 1
            else:
                num = ''
                while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                    num += expression[i]
                    i += 1
                tokens.append(num)
        return tokens

    def infix_to_postfix(self, expression):
        self.stack = []
        self.output = []
        tokens = self.tokenize(expression)

        for token in tokens:
            if self.is_operand(token):
                self.output.append(token)
            elif token == '(':
                self.stack.append(token)
            elif token == ')':
                while self.stack and self.stack[-1] != '(':
                    self.output.append(self.stack.pop())
                if self.stack:
                    self.stack.pop() 
            else: 
                while (self.stack and self.stack[-1] != '(' and
                       (self.precedence(self.stack[-1]) > self.precedence(token) or
                        (self.precedence(self.stack[-1]) == self.precedence(token) and
                         not self.is_right_associative(token)))):
                    self.output.append(self.stack.pop())
                self.stack.append(token)

        while self.stack:
            self.output.append(self.stack.pop())

        return ' '.join(self.output)


def evaluate_postfix(postfix):
    stack = []
    tokens = postfix.split()

    for token in tokens:
        if token in '+-*/^':
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)
            elif token == '^':
                stack.append(a ** b)
        else:
            stack.append(float(token))

    return stack[0]


if __name__ == "__main__":
    expression = "3.5+5*(2^3-40.11)^(2*1*2.0)-8.5"
    converter = Infix2Postfix()
    postfix = converter.infix_to_postfix(expression)
    print( evaluate_postfix(postfix))
   