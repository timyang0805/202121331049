import sys

def load(file_path):
    with open(file=file_path,mode='r',encoding="utf-8") as file:
        return file.read()
    

def calculate_similarity(orig_text,orig_add_text):
    

    words_orig = [char for char in orig_text]#将句子分割成单个字
    #print("words_orig=",words_orig)
    words_orig_add = [char for char in orig_add_text] #将句子分割成单个字
    #print("words_orig_add",words_orig_add)
    total_words = len(words_orig)#原文的字符串的长度
    #print("total_words",total_words)
    matcaed_words=0#抄袭的字符串长度

    for word in words_orig_add:
        if word in words_orig:
            matcaed_words +=1

    #print("matcaed_words=",matcaed_words)
    similarity = (matcaed_words/total_words) * 100 #匹配率并保留两位小数
    return similarity

def main():
    if len(sys.argv) != 4:
        print("Usage: python plagiarism_checker.py <original_file> <plagiarized_file> <output_file>")
        return 
    
    orig_file = sys.argv[1]#原文文件的路径
    orig_add_file = sys.argv[2]#抄袭文件的路径
    ans_file=sys.argv[3]
    orig_text=load(orig_file)
    orig_add_text=load(orig_add_file)

    ans=calculate_similarity(orig_text,orig_add_text)
    ans=round(ans,2)

    with open(file=ans_file,mode='w',encoding="utf-8") as file:
        file.write(f"Similarity: {ans}%\n")

    print(f"Similarity: {ans}%")

if __name__ == '__main__':
    main()
    

