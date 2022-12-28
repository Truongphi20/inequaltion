import unittest
import sinequal as sin

class TestSinequal(unittest.TestCase):

	def test_Solve_Inequal(self):

		biens = ["a","b","M","P"] # Khai báo tên biến
		cuctri = [0,0,-1,1]	# Khai báo biến có phải cực trị (0: không phải, 1: cực đại, -1: cực tiểu)
		he_bpt = ["2*a+b<=6","a+b>=0","a-b>=1","a+b-P==0","a-b-M==0"]

		result = sin.Solve_Inequal(biens, cuctri, he_bpt)

		self.assertEqual(result,(['a', 'b', 'M', 'P'], [[2, 1, 1, 3]]))

		biens = ["m","g","h","c","G"] # Khai báo tên biến
		cuctri = [0,0,0,0,1]	# Khai báo biến có phải cực trị (0: không phải, 1: cực đại, -1: cực tiểu)
		he_bpt = ["2*m+5*g+7*h+10*c<=100","2*m+5*g+10*h+15*c<=50", "4*m+8*g+11*h+19*c-G==0",
			"m>=1","g>=1","h>=1","c>=1"]

		result = sin.Solve_Inequal(biens, cuctri, he_bpt)

		self.assertEqual(result,(['m', 'g', 'h', 'c', 'G'], [[10, 1, 1, 1, 78]]))


		biens = ["h","c","w","b","W"] # Đặt ẩn tương ứng là lượng item lấy ở từng item
		cuctri = [0,0,0,0,-1]

		he_bpt = ["5*h+7*c+6*w+3*b-W==0", # Tổng khối lượng hàng hóa phải bé hơn 3kg
		            "W<=6","W>=1",
		            "h>=0","c>=0", # Các lượng item phải lớn hơn hoặc bằng 0
		            "w>=0","b>=0"]
		result = sin.Solve_Inequal(biens, cuctri, he_bpt)

		self.assertEqual(result,(['h', 'c', 'w', 'b', 'W'], [[0, 0, 0, 1, 3]]))


		biens = ["h","b","S","W"] # Đặt ẩn tương ứng là lượng item lấy ở từng item
		cuctri = [0,0,1,-1]

		he_bpt = ["10*h+7*b-W==0", # Tổng khối lượng hàng hóa phải bé hơn 3kg
		            "W<=20","W>=1",
		            "15*h+10*b-S==0", # Tong score phai lon nhat
		            "h>=0", # Các lượng item phải lớn hơn hoặc bằng 0
		            "b>=0"]
		result = sin.Solve_Inequal(biens, cuctri, he_bpt)

		self.assertEqual(result,(['h', 'b', 'S', 'W'], [[0, 1, 10, 7]]))

if __name__ == '__main__':
	unittest.main()