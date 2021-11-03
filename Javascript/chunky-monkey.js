function chunkArrayInGroups(arr, size) {
  let temp=[];
  let aux=[];
  let aux2=0;
    for(let i=0;i<=arr.length-1;i++){console.log(temp," order ",aux,i, " in ",aux2);
      aux.push(arr[i]);
      
      if(aux2 == size-1){console.log(i,"par", aux2,"wt", aux)
        aux2=-1;
        temp.push(aux);//add all
        aux=[];
      }
      if(i >= arr.length-1){console.log("exit");
        if(aux[0] != undefined){
          temp.push(aux);//add final
        }
        break;
      }
      aux2++;
    }
    console.log(temp," order ",aux);
  return temp;
}

chunkArrayInGroups(["a", "b", "c", "d"], 2);