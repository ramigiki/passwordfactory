# use nginx image
FROM nginx

# remove defaults
RUN rm /etc/nginx/conf.d/default.conf

# replace nginx.conf
COPY docker/nginx/nginx.conf /etc/nginx/conf.d/
