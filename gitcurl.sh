if [ "$#" -lt 4 ]; then
	echo "Usage gitcurl.sh <username> <repo-name> <repo-desc> <(Private): true|false>\nYou will be prompted for your API key"
	exit 1
fi 
curl -u "$1" https://api.github.com/user/repos -d "{\"name\":\"$2\",\"description\":\"$3\",\"private\":$4}"


