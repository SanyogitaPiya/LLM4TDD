def code(self, words: List[str]) -> int:
        # Sort the list in descending order based on length
        words.sort(key=len, reverse=True)

        # Initialize the encoded string
        st = ""

        # Traverse the array and update the encoded string
        for word in words:
            if word + "#" not in st:
                st += word + "#"

        # Return the length of the encoded string
        return len(st)
