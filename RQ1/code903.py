def a(s):
    segments = []
    segment_type = None
    count = 1

    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            if segment_type is not None:
                segments.append((segment_type, count))
            segment_type = s[i]
            count = 1
        else:
            count += 1

    segments.append((segment_type, count))  # Add the last segment

    result = segments[0][1] + 1  # Adding the first segment

    for i in range(1, len(segments)):
        if segments[i][0] == 'T':
            result += max(segments[i-1][1], segments[i][1]) + 1
        else:
            result += segments[i][1] + 1

    return result

