import webbrowser


def generate_report(jobs):
    def print_jobs():
        string = "<table class='table'>"
        string += '''<thead><tr>
            <th>#</th>
            <th scope="col">Kompanija</th>
            <th scope="col">Pozicija</th>
            <th scope="col">Užmokėstis</th>
            <th scope="col">Nuoroda</th>
            </tr></thead>'''
        string += "<tbody>"
        for idx, job in enumerate(jobs):
            string += "<tr>"
            string += "<th>" + str(idx + 1) + "</th>"
            string += "<td>" + job.company + "</td>"
            string += "<td>" + job.position + "</td>"
            string += "<td>" + job.salary + "</td>"
            string += "<td><button class='btn btn-primary'><a href='" + \
                job.link + "'>Skelbimas</a></button></td>"
            string += "</th>"
        string += "</tbody>"
        string += "</table>"
        return string

    html_string = '''
    <!DOCTYPE html>
    <html>
        <head>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.bundle.min.js" integrity="sha384-b5kHyXgcpbZJO/tY9Ul7kGkf1S0CWuKcCD38l8YkeH8z8QjE0GmW1gYU5S9FOnJ0" crossorigin="anonymous"></script>
            <style>body{ margin:0 100; background:whitesmoke; } 
            a{color:white; text-decoration: none}
            a:hover { color: inherit;}
            </style>
        </head>
        <body>
            <h1>Dabartiniai CVBankas darbų pasiūlymai</h1>
            ''' + print_jobs() + '''
        </body>
    </html>'''

    f = open('./report.html', 'w')
    f.write(html_string)
    f.close()

    webbrowser.open('./report.html')
