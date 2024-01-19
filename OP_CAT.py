def OP_CAT (Stack1,Stack2):
    Stack3 = Stack1 + Stack2
    return Stack3

Stack1 = "Taproot "
Stack2 = "Saved OP_CAT"

Message = OP_CAT(Stack1,Stack2)
print(Message)