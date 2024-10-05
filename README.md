## AWS SAM テンプレート

AWS SAM に個人的な改良を加えたテンプレートです。

- 独自 CloudWatch Logs ロググループの追加
- Lambda 関数の標準的な監視のための CloudWatch アラーム
- Secrets Manger
- CloudWatch Event スケジューラのサンプル設定
- 上記を使うための独自 IAM ロールと関数へのアタッチ

# 使い方

## デプロイ

```
sam deploy --parameter-overrides Stage=[ prod | stg | dev | test ]
```
