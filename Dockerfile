FROM nginx
RUN chown nginx /var/cache/nginx
RUN chown nginx /var/run
RUN sed -i -e '/listen/!b' -e '/80;/!b' -e 's/80;/8080;/' /etc/nginx/conf.d/default.conf
USER nginx
COPY . /usr/share/nginx/html
EXPOSE 8080
# ENTRYPOINT [“/usr/sbin/nginx”]