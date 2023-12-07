class Solution:
    def code(self, num: int) -> str:
        if num == 0:
            return "Zero"

        result = ""
        billion_names = ["", "One Billion", "Two Billion"]
        million_names = ["", "One Million", "Two Million"]
        thousand_names = ["", "One Thousand", "Two Thousand"]
        tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        units = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        teens = ["", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

        # Updated function to convert a three-digit number to words
        def convert_three_digits(num):
            hundreds_digit = num // 100
            remaining_digits = num % 100

            result_str = ""
            if hundreds_digit > 0:
                result_str += f"{units[hundreds_digit]} Hundred "

            if remaining_digits == 0:
                return result_str.strip()
            elif remaining_digits == 10:
                result_str += "Ten"
            elif remaining_digits < 10:
                result_str += units[remaining_digits]
            elif remaining_digits < 20:
                result_str += teens[remaining_digits - 10]
            else:
                tens_digit = remaining_digits // 10
                units_digit = remaining_digits % 10
                result_str += f"{tens[tens_digit]} {units[units_digit]}"

            return result_str.strip()

        # Convert billions, millions, and thousands
        if num >= 1000000000:
            result += f"{convert_three_digits(num // 1000000000)} Billion "
            num %= 1000000000

        if num >= 1000000:
            result += f"{convert_three_digits(num // 1000000)} Million "
            num %= 1000000

        if num >= 1000:
            result += f"{convert_three_digits(num // 1000)} Thousand "
            num %= 1000

        # Convert the remaining hundreds
        if num > 0:
            result += convert_three_digits(num)

        return result.strip()


