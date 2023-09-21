import "fmt"

func convert(s string, numRows int) string {
	if numRows == 1 {
		return s
	}
	x := make([]string, numRows)
	cnt := 0
	flg := false
	for i := 0; i < len(s); i++ {
		//fmt.Println(cnt," ",i," ",string(s[i]),"  ",flg)
		x[cnt] = x[cnt] + string(s[i])
		if flg == false {
			cnt += 1
		} else {
			cnt -= 1
		}
		if cnt >= numRows {
			flg = true
			cnt -= 2
		}
		if cnt == 0 {
			flg = false
		}
	}
	result := ""
	for i := 0; i < len(x); i++ {
		result += x[i]
	}
	return result
}