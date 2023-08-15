#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
bool solution(const char* s) {
    bool answer = true;
    
    int len = strlen(s);
    
    int ncount = 0;
    for(int i = 0; i < len; i++)
    {
        if(s[i] == '(')
        {
            ncount++;
        }
        else
        {
            if(ncount == 0)
                return false;
            else
                ncount--;
        }
    }
    
    answer = (ncount == 0) ? true : false;
    
    return answer;
}