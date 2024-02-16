from Flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data for Words Shop and Words Bucket
words_shop = ["Word 1", "Word 2", "Word 3"]
words_bucket = []

# GET request to fetch words from Words Shop
@app.route('/words-shop', methods=['GET'])
def get_words_shop():
    return jsonify(words_shop)

# POST request to move a word from Words Shop to Words Bucket
@app.route('/move-to-bucket', methods=['POST'])
def move_to_bucket():
    word = request.json.get('word')
    if word in words_shop:
        words_shop.remove(word)
        words_bucket.append(word)
        return jsonify({"message": "Word moved to bucket successfully"})
    else:
        return jsonify({"error": "Word not found in Words Shop"}), 404

# PUT request to mark a word in Words Bucket as learned
@app.route('/mark-as-learned/<string:word>', methods=['PUT'])
def mark_as_learned(word):
    if word in words_bucket:
        # Assuming you want to remove the word from bucket after marking as learned
        words_bucket.remove(word)
        return jsonify({"message": "Word marked as learned successfully"})
    else:
        return jsonify({"error": "Word not found in Words Bucket"}), 404

# DELETE request to delete a word from Words Bucket
@app.route('/delete-from-bucket/<string:word>', methods=['DELETE'])
def delete_from_bucket(word):
    if word in words_bucket:
        words_bucket.remove(word)
        return jsonify({"message": "Word deleted from bucket successfully"})
    else:
        return jsonify({"error": "Word not found in Words Bucket"}), 404

# DELETE request to delete all learned words from Words Bucket
@app.route('/delete-all-learned', methods=['DELETE'])
def delete_all_learned():
    global words_bucket
    words_bucket = [word for word in words_bucket if word not in words_shop]
    return jsonify({"message": "All learned words deleted from bucket successfully"})

if __name__ == '__main__':
    app.run(debug=True)
