package repository;
import domain.Identifiable;
import java.util.HashMap;
import java.util.Map;

public class MemoryRepository<T extends Identifiable,U> implements IRepository<T,U>{
     Map<Integer, T> data = new HashMap<>();
    @Override
    public void add(T elem) {
        if (elem != null && !data.containsKey(elem.getId())) {
            data.put(elem.getId(), elem);
        } else {
            throw new IllegalArgumentException("The entity is invalid .");
        }
    }

    @Override
    public void update(T elem)
    {
        if (elem != null && data.containsKey(elem.getId())) {
            data.put(elem.getId(), elem);
        } else {
            throw new IllegalArgumentException("The entity not found or invalid.");
        }
    }



    public void remove(Integer id)
    {
        if (id != null) {
            T removedItem = data.remove(id);
            if (removedItem == null) {
                throw new IllegalArgumentException("The entity not found or invalid ID.");
            }
        }
    }

    @Override
    public T findbyid(Integer id)
    {
        if (id != null) {
            return data.get(id);
        }
        return null;
    }

    @Override
    public boolean exists(Integer id)
    {
        return data.containsKey(id);
    }

    @Override
    public Iterable<T> getAll()
    {
        return data.values();
    }
}
