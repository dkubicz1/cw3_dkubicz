import subprocess
import json

def run_curl_command(url):
    result = subprocess.run(['curl', '-s', url], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout, result.stderr, result.returncode

def check_response(response, key_to_check):
    try:
        response_json = json.loads(response)
        if isinstance(response_json, list):
            response_json = response_json[0]  # Sprawdzamy pierwszy element listy
        return response_json, key_to_check in response_json
    except json.JSONDecodeError:
        return None, False

def test_endpoint(url, key_to_check):
    response, error, returncode = run_curl_command(url)
    if returncode != 0:
        print(f"Error calling {url}: {error.decode()}")
        return False

    response_json, key_present = check_response(response, key_to_check)
    if key_present:
        print(f"Test {url}: PASSED")
        return True
    else:
        print(f"Test {url}: FAILED")
        return False

def main():
    api_base_url = 'https://jsonplaceholder.typicode.com'
    endpoints = [
        ('/posts', 'userId'),
        ('/comments', 'postId'),
        ('/users', 'id')
    ]

    all_tests_passed = True
    for endpoint, key_to_check in endpoints:
        url = f"{api_base_url}{endpoint}"
        if not test_endpoint(url, key_to_check):
            all_tests_passed = False

    if all_tests_passed:
        print("All tests PASSED")
    else:
        print("Some tests FAILED")

if __name__ == "__main__":
    main()
