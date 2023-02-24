if [ $# -ne 2 ]; then
  echo "引数が一致しません"
  echo "使用方法: ./nm_search.sh ファイル　検索シンボル"
  exit 1
fi
for file in $1; do
	echo "${file}"
	nm ${file} | grep $2
done 
