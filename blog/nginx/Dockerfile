FROM nginx:latest
COPY nginx.conf /etc/nginx/nginx.conf
COPY blog.nginx.conf /etc/nginx/sites-available/blog.nginx.conf
RUN mkdir /etc/nginx/sites-enabled
RUN ln -s /etc/nginx/sites-available/blog.nginx.conf /etc/nginx/sites-enabled/
CMD ["nginx", "-g", "daemon off;"]