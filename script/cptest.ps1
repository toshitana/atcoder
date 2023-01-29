
$problem_name = $Args[0]
$problem_name_list = ($problem_name -split "_")
$base_url = ($problem_name.Replace("_", "-")).Substring(0, ($problem_name.Length) - 2)

if (! (Test-Path $test_dir)) {
    oj dl -d test/$problem_name/ https://atcoder.jp/contests/$base_url/tasks/$problem_name
}

oj test -c "python src/$problem_name.py" -d test/$problem_name/