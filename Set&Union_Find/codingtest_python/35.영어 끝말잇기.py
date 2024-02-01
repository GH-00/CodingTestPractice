def solutiom(n, words):
    used_words = set() # 이미 사용한 단어를 저장하는 set
    prev_word = words[0][0] #이전 단어의 마지막 글자

    for i, word in enumerate(words):
        # 이미 사용한 단어거나 첫 글자가 이전 단어와 일치하지 않으면
        if word in used_words or word[0] != prev_word:
            # 탈락하는 사람의 번호와 차례를 반환
            return [(i % n) + 1, (i // n) + 1]
        used_words.add(word) # 사용한 단어로 추가
        prev_word = word[-1] # 이전 단어의 마지막 글자 업데이트
    return [0,0] # 모두 통과했을 경우 반환값