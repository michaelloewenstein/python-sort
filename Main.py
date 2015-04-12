import DbManager
import ConfigManager
import SortManager

config = ConfigManager.ConfigManager()
db = DbManager.DbManager(config)

arr = [2,3,4,6,1,9]
inputarr = arr
SortManager.SortManager.quickSort(arr,0,5)		
db.insert(inputarr,arr,'quicksort2')
print(arr)