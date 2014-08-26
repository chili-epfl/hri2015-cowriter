from subprocess import check_output
import json

DOCUMENT_ID="1159230fytxkw"

curl = "curl 'https://www.writelatex.com/docs/{id}/srcs/2765322/latest.json' -H 'Host: www.writelatex.com' -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0' -H 'Accept: */*' -H 'Accept-Language: en-US,en;q=0.5' -H 'Accept-Encoding: gzip, deflate' -H 'DNT: 1' -H 'X-CSRF-Token: 33T9lFwmFK4qc8w7t7n+5/zRH/dl4nreCy+rmYwe3XA=' -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H 'X-Requested-With: XMLHttpRequest' -H 'Referer: https://www.writelatex.com/{id}' -H 'Cookie: hide_help_ride=true; wl_editor_position=59.84395477334606%2525; remember_user_token=BAhbB1sGaQKdSUkiIiQyYSQxMCRpNmlCU0RCREg3MHlBeXg4aC5tT2V1BjoGRVQ%3D--5bb2cac5ccedfcf6181ed9207ccec8b05f0f852e; wl_project_open=false; _write_latex_session=BAh7CEkiD3Nlc3Npb25faWQGOgZFVEkiJWJlMWNiODQ5ZGJhMzVlOTA2Yzc2OTk2YTkyZmFlOTI1BjsAVEkiGXdhcmRlbi51c2VyLnVzZXIua2V5BjsAVFsHWwZpAp1JSSIiJDJhJDEwJGk2aUJTREJESDcweUF5eDhoLm1PZXUGOwBUSSIQX2NzcmZfdG9rZW4GOwBGSSIxMzNUOWxGd21GSzRxYzh3N3Q3bis1L3pSSC9kbDRucmVDeStybVl3ZTNYQT0GOwBG--36750f6aacee3bbfd91f468f5f084d2a6d12b4bd; wl_cm_cursor_2765322=%7B%22line%22%3A723%2C%22ch%22%3A34%2C%22xRel%22%3A1%7D' -H 'Connection: keep-alive' -H 'Pragma: no-cache' -H 'Cache-Control: no-cache' --data 'protocolVersion=4&saved_ver_id='".format(id = DOCUMENT_ID)

rawtexfile = check_output(curl, shell=True)

texfile = json.loads(rawtexfile)["content"].encode("utf8")

print(texfile)
