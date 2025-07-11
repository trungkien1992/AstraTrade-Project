#!/usr/bin/env python3
"""
Test the complete task flow for code-aware indexing
"""

import time
import requests
import json

BASE_URL = "http://localhost:8000"

def test_complete_task_flow():
    """Test complete task flow from start to finish"""
    print("Testing complete task flow...")
    
    # 1. Start the task
    try:
        response = requests.post(f"{BASE_URL}/index/code_aware")
        if response.status_code != 200:
            print(f"❌ Failed to start task: {response.status_code}")
            return False
        
        task_info = response.json()
        task_id = task_info["task_id"]
        print(f"✅ Started task: {task_id}")
        print(f"Initial response: {task_info['status']}")
        
        # 2. Check initial status (should be in_progress)
        status_response = requests.get(f"{BASE_URL}/status/{task_id}")
        if status_response.status_code != 200:
            print(f"❌ Failed to get initial status: {status_response.status_code}")
            return False
        
        status = status_response.json()
        print(f"Initial status: {status['status']}")
        print(f"Operation: {status['operation']}")
        print(f"Start time: {status['start_time']}")
        
        # 3. Poll status until completion
        max_polls = 10
        poll_count = 0
        
        while poll_count < max_polls:
            time.sleep(1)
            poll_count += 1
            
            status_response = requests.get(f"{BASE_URL}/status/{task_id}")
            if status_response.status_code != 200:
                print(f"❌ Failed to get status on poll {poll_count}: {status_response.status_code}")
                return False
            
            status = status_response.json()
            print(f"Poll {poll_count}: {status['status']}")
            
            if status["status"] == "completed":
                print(f"✅ Task completed successfully!")
                print(f"Time taken: {status.get('time_taken', 'unknown')}s")
                print(f"Result: {status.get('result', {})}")
                return True
            elif status["status"] == "failed":
                print(f"❌ Task failed: {status.get('error', 'unknown error')}")
                return False
        
        print(f"⏳ Task still running after {max_polls} polls")
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

def test_multiple_tasks():
    """Test multiple concurrent tasks"""
    print("\nTesting multiple concurrent tasks...")
    
    task_ids = []
    
    # Start multiple tasks
    for i in range(3):
        try:
            response = requests.post(f"{BASE_URL}/index/code_aware")
            if response.status_code == 200:
                task_info = response.json()
                task_ids.append(task_info["task_id"])
                print(f"Started task {i+1}: {task_info['task_id']}")
            else:
                print(f"❌ Failed to start task {i+1}: {response.status_code}")
        except Exception as e:
            print(f"❌ Error starting task {i+1}: {e}")
    
    # Check all task statuses
    print(f"\nChecking status of {len(task_ids)} tasks...")
    for i, task_id in enumerate(task_ids):
        try:
            status_response = requests.get(f"{BASE_URL}/status/{task_id}")
            if status_response.status_code == 200:
                status = status_response.json()
                print(f"Task {i+1} ({task_id[:8]}...): {status['status']}")
            else:
                print(f"❌ Failed to get status for task {i+1}: {status_response.status_code}")
        except Exception as e:
            print(f"❌ Error checking task {i+1}: {e}")
    
    return len(task_ids) > 0

if __name__ == "__main__":
    print("Testing Complete Task Flow")
    print("=" * 40)
    
    # Test complete flow
    success1 = test_complete_task_flow()
    
    # Test multiple tasks
    success2 = test_multiple_tasks()
    
    print(f"\nResults:")
    print(f"Complete flow test: {'✅ PASSED' if success1 else '❌ FAILED'}")
    print(f"Multiple tasks test: {'✅ PASSED' if success2 else '❌ FAILED'}")
    
    if success1 and success2:
        print("\n🎉 All task flow tests passed!")
    else:
        print("\n⚠️  Some tests failed")