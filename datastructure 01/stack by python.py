'''
[C언어 원본 코드]
int eval(char exp[])
{
    int op1, op2, value, i = 0;
    int len = strlen(exp);
    char ch;
    StackType s;

    init_stack(&s);
    for (i = 0; i < len; i++) {
        ch = exp[i];
        if (ch != '+' && ch != '-' && ch != '*' && ch != '/') {
            value = ch - '0'; // 입력이 피연산자이면
            push(&s, value);
        }
        else { // 연산자이면 피연산자를 스택에서 제거
            op2 = pop(&s);
            op1 = pop(&s);
            switch (ch) { // 연산을 수행하고 스택에 저장
            case '+': push(&s, op1 + op2); break;
            case '-': push(&s, op1 - op2); break;
            case '*': push(&s, op1 * op2); break;
            case '/': push(&s, op1 / op2); break;
            }
        }
    }
    return pop(&s);
}
'''

def eval(exp):
    op1 = 0
    op2 = 0
    value = 0
    length = len(exp)
    s = []

    for i in range(length):
        ch = exp[i]

        if ch != '+' and ch != '-' and ch != '*' and ch != '/':
            value = int(ch)
            s.append(value)
        else:
            op2 = s.pop()
            op1 = s.pop()

            if ch == '+':
                s.append(op1 + op2)
            elif ch == '-':
                s.append(op1 - op2)
            elif ch == '*':
                s.append(op1 * op2)
            elif ch == '/':
                s.append(int(op1 / op2))

    return s.pop()
exp = "123*-"
print(eval(exp))