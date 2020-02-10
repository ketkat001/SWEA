def password(m):
    m_list = []
    for x in range(len(m)):
        m_list.append(m[x])
    while(True):
        for i in range(len(m_list)-1):
            if m_list[i] == m_list[i+1]:
                m_list.pop(i)
                m_list.pop(i)
                break
        else:
            break
    return ''.join(map(str, m_list))

for t in range(1, 11):
    N, M = input().split()
    print('#{} {}'.format(t, password(M)))
