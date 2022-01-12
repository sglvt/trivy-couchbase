# trivy-couchbase
## Start Couchbase
```
podman run -d --name cdb-702 -p 8091-8094:8091-8094 -p 11210:11210 public.ecr.aws/docker/library/couchbase:community-7.0.2
```

## Create Couchbase bucket and index
Access the console at http://localhost:8091/ui/
Create a bucket named `trivy`
Create primary index
```
CREATE PRIMARY INDEX ON `default`:`trivy`
CREATE INDEX target ON `trivy`(Target)
```

## Scan an image and write output to a file
```
trivy i --format json -o scan.json docker.io/alpine:3.12
```

## Create venv and run the script
```
python3 -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

read -p "COUCHBASE_USER=" COUCHBASE_USER
read -sp "COUCHBASE_PASSWORD=" COUCHBASE_PASSWORD
export COUCHBASE_USER=${COUCHBASE_USER}
export COUCHBASE_PASSWORD=${COUCHBASE_PASSWORD}

python cb.py
```

## Query
```
select Target,Vulnerabilities from `trivy` 
where Target like "%alpine%"
and any v in Vulnerabilities satisfies v.Severity="CRITICAL" end;
```