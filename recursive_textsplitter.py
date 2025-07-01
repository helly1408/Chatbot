from langchain.text_splitter import RecursiveCharacterTextSplitter
text=""" The old bookstore at the corner of Maple Street had a charm that couldn’t be replicated. Dusty shelves stretched from floor to ceiling, crammed with novels, journals, and forgotten tales waiting to be rediscovered. A bell above the door chimed softly whenever someone entered, breaking the silence like a whisper. The scent of aged paper mixed with the faint aroma of coffee from the back room, where a cat named Whiskers often lounged on a sunny windowsill. It was a place where time seemed to slow down, inviting visitors to lose themselves in the magic of words and imagination."""
splitter=RecursiveCharacterTextSplitter(
    chunk_size=30,
    chunk_overlap=0,
)
chunks=splitter.split_text(text)
print(len(chunks))
print(chunks)