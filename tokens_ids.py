import tiktoken
def get_input():
    return input("Enter input: ")

def report_tokens(answer):
    encoding = tiktoken.get_encoding("cl100k_base")
    token_ids = encoding.encode(answer)
    token_count = len(token_ids)

    pieces = []
    for token_id in token_ids:
        piece_bytes = encoding.decode_single_token_bytes(token_id)
        pieces.append(piece_bytes.decode('utf-8', errors = 'replace'))

    print(f"Input: {answer}")
    print(f"Token count: {token_count}")
    print(f"Decoded pieces: {pieces}")
    print(f"Token IDs: {token_ids}")

answer = get_input()
report_tokens(answer)