function findDuplicate(nums) {
  let i = 0;

  while (i < nums.length) {
    if (nums[i] !== i + 1) {
      let j = nums[i] - 1;
      if (nums[i] !== nums[j]) {
        //swap
        [nums[i], nums[j]] = [nums[j], nums[i]];
      } else {
        //we have found the duplicate
        return nums[i];
      }
    } else {
      i++;
    }
  }
  return -1;
}
