package seegah

func Atoi(s string) int {
	result, sign := 0, 1
	for i, c := range s {
		if i == 0 && (c == '-' || c == '+') {
			if c == '-' {
				sign = -1
			}
			continue
		}
		if c < '0' || c > '9' {
			return 0
		}
		result = result*10 + int(c-'0')
	}
	return result * sign
}
