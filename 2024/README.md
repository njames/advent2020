# Set up new year

from root directory 

```bash
mkcdir year
mkcdir python
for num in {1..24}; do    value=$(printf "%02d" $num);  mkdir day$value;  done;

mkcdir ../input
for num in {1..24}; do    value=$(printf "%02d" $num);  mkdir day$value;  done;

```

