def czy_przestepny(rok):
    if rok % 4 == 0:
        if rok % 100 == 0:
            if rok % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Testowanie funkcji
rok = 2000
if czy_przestepny(rok):
    print(f"{rok} jest rokiem przestępnym.")
else:
    print(f"{rok} nie jest rokiem przestępnym.")