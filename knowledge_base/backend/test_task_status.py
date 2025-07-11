#!/usr/bin/env python3
"""
Test script for task status tracking functionality
"""

import time
import requests
import json
from typing import Dict, Any

BASE_URL = "http://localhost:8000"

def test_index_task_status():
    """Test indexing task status tracking"""
    print("Testing indexing task status tracking...")
    
    # Start indexing task
    index_data = {"force_reindex": False}
    try:
        response = requests.post(f"{BASE_URL}/index", json=index_data)
        if response.status_code == 200:
            task_info = response.json()
            task_id = task_info["task_id"]
            print(f"✅ Started indexing task: {task_id}")
            
            # Check initial status
            status_response = requests.get(f"{BASE_URL}/status/{task_id}")
            if status_response.status_code == 200:
                status = status_response.json()
                print(f"Initial status: {status['status']}")
                print(f"Operation: {status['operation']}")
                
                # Wait and check status again
                time.sleep(2)
                status_response = requests.get(f"{BASE_URL}/status/{task_id}")
                if status_response.status_code == 200:
                    status = status_response.json()
                    print(f"Status after 2s: {status['status']}")
                    
                    if status["status"] == "completed":
                        print(f"✅ Task completed in {status.get('time_taken', 'unknown')}s")
                        print(f"Documents indexed: {status.get('documents_indexed', 'unknown')}")
                        return True
                    elif status["status"] == "failed":
                        print(f"❌ Task failed: {status.get('error', 'unknown error')}")
                        return False
                    else:
                        print(f"⏳ Task still in progress: {status['status']}")
                        return True
                else:
                    print(f"❌ Failed to get task status: {status_response.status_code}")
                    return False
            else:
                print(f"❌ Failed to get initial status: {status_response.status_code}")
                return False
        else:
            print(f"❌ Failed to start indexing task: {response.status_code}")
            if response.status_code == 401:
                print("Note: This endpoint requires API key authentication")
            return False
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

def test_optimize_task_status():
    """Test optimization task status tracking"""
    print("\nTesting optimization task status tracking...")
    
    try:
        response = requests.post(f"{BASE_URL}/optimize")
        if response.status_code == 200:
            task_info = response.json()
            task_id = task_info["task_id"]
            print(f"✅ Started optimization task: {task_id}")
            
            # Check status
            status_response = requests.get(f"{BASE_URL}/status/{task_id}")
            if status_response.status_code == 200:
                status = status_response.json()
                print(f"Status: {status['status']}")
                print(f"Operation: {status['operation']}")
                return True
            else:
                print(f"❌ Failed to get task status: {status_response.status_code}")
                return False
        else:
            print(f"❌ Failed to start optimization task: {response.status_code}")
            if response.status_code == 401:
                print("Note: This endpoint requires API key authentication")
            return False
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

def test_code_aware_indexing_task_status():
    """Test code-aware indexing task status tracking"""
    print("\nTesting code-aware indexing task status tracking...")
    
    try:
        response = requests.post(f"{BASE_URL}/index/code_aware")
        if response.status_code == 200:
            task_info = response.json()
            task_id = task_info["task_id"]
            print(f"✅ Started code-aware indexing task: {task_id}")
            
            # Check status
            status_response = requests.get(f"{BASE_URL}/status/{task_id}")
            if status_response.status_code == 200:
                status = status_response.json()
                print(f"Status: {status['status']}")
                print(f"Operation: {status['operation']}")
                return True
            else:
                print(f"❌ Failed to get task status: {status_response.status_code}")
                return False
        else:
            print(f"❌ Failed to start code-aware indexing task: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

def test_invalid_task_id():
    """Test handling of invalid task IDs"""
    print("\nTesting invalid task ID handling...")
    
    try:
        fake_task_id = "invalid-task-id-12345"
        response = requests.get(f"{BASE_URL}/status/{fake_task_id}")
        if response.status_code == 404:
            print("✅ Correctly returned 404 for invalid task ID")
            return True
        else:
            print(f"❌ Expected 404, got {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

def test_server_health():
    """Test if server is running"""
    print("Checking server health...")
    
    try:
        response = requests.get(f"{BASE_URL}/")
        if response.status_code == 200:
            print("✅ Server is running")
            return True
        else:
            print(f"❌ Server returned {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Server not accessible: {e}")
        return False

if __name__ == "__main__":
    print("Testing Task Status Tracking System")
    print("=" * 50)
    
    # Test server health first
    if not test_server_health():
        print("❌ Server not accessible. Make sure the server is running.")
        exit(1)
    
    # Run tests
    tests = [
        test_invalid_task_id,
        test_index_task_status,
        test_optimize_task_status,
        test_code_aware_indexing_task_status
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
    
    print(f"\nTest Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("✅ All task status tracking tests passed!")
    else:
        print(f"⚠️  {total - passed} tests failed or require API key")