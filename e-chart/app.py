from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)


@app.route('/api/data/<name>')
def get_data(name):
    try:
        path = f'data/{name}.csv'
        print("🔍 正在尝试读取文件：", path)
        df = pd.read_csv(path)
        return df.to_json(orient='records', force_ascii=False)
    except Exception as e:
        print("❌ 错误信息：", e)
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
